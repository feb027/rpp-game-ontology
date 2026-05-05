#!/usr/bin/env python3
"""Patch live Caddy admin config for RPP Streamlit deployment.

Adds:
- iot.aquarise.my.id/rpp-game/* -> localhost:8515
- rpp-game.aquarise.my.id/* -> localhost:8514

Note: this changes Caddy's live admin config. Persist the same routes in
/etc/caddy/Caddyfile separately if the machine restarts.
"""
from __future__ import annotations

import json
import urllib.request

ADMIN = "http://127.0.0.1:2019"


def get_json(path: str):
    with urllib.request.urlopen(ADMIN + path, timeout=10) as r:
        return json.load(r)


def post_json(path: str, data) -> None:
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(
        ADMIN + path,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        r.read()


def headers_handler():
    return {
        "handler": "headers",
        "response": {
            "deferred": True,
            "delete": ["Server"],
            "set": {
                "X-Content-Type-Options": ["nosniff"],
                "X-Frame-Options": ["SAMEORIGIN"],
                "Referrer-Policy": ["strict-origin-when-cross-origin"],
            },
        },
    }


def encode_handler():
    return {
        "handler": "encode",
        "encodings": {"gzip": {}, "zstd": {}},
        "prefer": ["gzip", "zstd"],
    }


def proxy_route_for_path(path_pattern: str, upstream: str):
    return {
        "match": [{"path": [path_pattern]}],
        "handle": [
            headers_handler(),
            encode_handler(),
            {"handler": "reverse_proxy", "upstreams": [{"dial": upstream}]},
        ],
    }


def host_route(host: str, upstream: str):
    return {
        "match": [{"host": [host]}],
        "handle": [
            {
                "handler": "subroute",
                "routes": [
                    {
                        "handle": [
                            headers_handler(),
                            encode_handler(),
                            {"handler": "reverse_proxy", "upstreams": [{"dial": upstream}]},
                        ]
                    }
                ],
            }
        ],
        "terminal": True,
    }


def route_hosts(route):
    hosts = []
    for m in route.get("match", []):
        hosts.extend(m.get("host", []))
    return hosts


def path_matches(route):
    paths = []
    for m in route.get("match", []):
        paths.extend(m.get("path", []))
    return paths


config = get_json("/config/")
routes = config["apps"]["http"]["servers"]["srv0"]["routes"]

# Add /rpp-game route under existing iot host route.
iot_route = next((r for r in routes if "iot.aquarise.my.id" in route_hosts(r)), None)
if iot_route is None:
    raise SystemExit("iot.aquarise.my.id route not found")
subroutes = iot_route["handle"][0]["routes"]
if not any("/rpp-game*" in path_matches(r) for r in subroutes):
    subroutes.insert(0, proxy_route_for_path("/rpp-game*", "localhost:8515"))
    print("added iot.aquarise.my.id/rpp-game route")
else:
    print("iot.aquarise.my.id/rpp-game route already exists")

# Add dedicated subdomain route; DNS still must point to this VPS.
if not any("rpp-game.aquarise.my.id" in route_hosts(r) for r in routes):
    routes.append(host_route("rpp-game.aquarise.my.id", "localhost:8514"))
    print("added rpp-game.aquarise.my.id route")
else:
    print("rpp-game.aquarise.my.id route already exists")

post_json("/load", config)
print("caddy admin config loaded")
