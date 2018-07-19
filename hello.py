from flask import Flask
from js9 import j
import json
app = Flask(__name__)

data = {
    'type': 'influxdb', 
    'access': 'proxy', 
    'database': "" , 
    'name': "", 
    'url': "", 
    'user': 'admin', 
    'password': 'passwd', 
    'default': True, 
}

password = "admin"
url = "http://localhost:3000"
username = "admin"
dashboard = """
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": false,
  "gnetId": null,
  "graphTooltip": 0,
  "id": 4,
  "links": [],
  "panels": [
    {
      "aliasColors": { },
      "bars": true,
      "dashLength": 10,
      "dashes": false,
      "datasource": "noaa",
      "fill": 1,
      "gridPos": {
        "h": 9,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 2,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": false,
      "linewidth": 1,
      "nullPointMode": "null",
      "percentage": false,
      "pointradius": 5,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "groupBy": [
            {
              "params": [
                "$__interval"
              ],
              "type": "time"
            },
            {
              "params": [
                "null"
              ],
              "type": "fill"
            }
          ],
          "measurement": "h2o_pH",
          "orderByTime": "ASC",
          "policy": "default",
          "query": "SELECT  *  FROM \\\"h2o_pH\\\" ",
          "rawQuery": true,
          "refId": "A",
          "resultFormat": "time_series",
          "select": [
            [
              {
                "params": [
                  "value"
                ],
                "type": "field"
              },
              {
                "params": [],
                "type": "mean"
              }
            ]
          ],
          "tags": []
        }
      ],
      "thresholds": [],
      "timeFrom": null,
      "timeShift": null,
      "title": "Panel Title",
      "tooltip": {
        "shared": false,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "buckets": null,
        "mode": "series",
        "name": null,
        "show": true,
        "values": [
          "count"
        ]
      },
      "yaxes": [
        {
          "format": "short",
          "label": null,
          "logBase": 1,
          "max": "10000",
          "min": "0",
          "show": true
        },
        {
          "format": "short",
          "label": null,
          "logBase": 1,
          "max": null,
          "min": null,
          "show": true
        }
      ],
      "yaxis": {
        "align": false,
        "alignLevel": null
      }
    }
  ],
  "schemaVersion": 16,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {
    "hidden": false,
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "timezone": "",
  "title": "dashboard",
  "uid": "Wd04I9dmz",
  "version": 1
  }
"""
@app.route('/')
def render_grafana():
    new_dashboard = ""
    if j.clients.grafana.get(data = {"password_" : password, "url" : url, "username" : username}):
        cl = j.clients.grafana.get(data = {"password_" : password, "url" : url, "username" : username})
    else:
        cl = j.clients.grafana.new('main', data = {"password_" : password, "url" : url, "username" : username})
            
    data["database"] = "noaa"
    data["name"] = ""
    data["url"] = ""


    cl.addDataSource(data)
    new_dashboard = cl.updateDashboard(dashboard)
    print(new_dashboard)
    return """
    <iframe src="http://localhost:3000/{0}" width="1000" height="1000" frameborder="0"></iframe>
    """.format(new_dashboard["url"])

