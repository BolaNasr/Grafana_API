from flask import Flask
import json 
from js9 import j
import signal
import time

import requests
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
        "datasource": " -- Grafana -- ", 
        "enable": true, 
        "hide": true, 
        "iconColor": "rgba(0, 211, 255, 1)", 
        "name": "Annotations & Alerts", 
        "type": "dashboard"
      }
    ]
  }, 
  "editable": true, 
  "gnetId": null, 
  "graphTooltip": 0, 
  "id": 2, 
  "links": [], 
  "panels": [
    {
      "aliasColors": {}, 
      "bars": false, 
      "dashLength": 10, 
      "dashes": false, 
      "datasource": null, 
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
        "show": true, 
        "total": false, 
        "values": false
      }, 
      "lines": true, 
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
        {}
      ], 
      "thresholds": [], 
      "timeFrom": null, 
      "timeShift": null, 
      "title": "Panel Title", 
      "tooltip": {
        "shared": true, 
        "sort": 0, 
        "value_type": "individual"
      }, 
      "type": "graph", 
      "xaxis": {
        "buckets": null, 
        "mode": "time", 
        "name": null, 
        "show": true, 
        "values": []
      }, 
      "yaxes": [
        {
          "format": "short", 
          "label": null, 
          "logBase": 1, 
          "max": null, 
          "min": null, 
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
  "title": "New dashboard Copy1111", 
  "uid": "DeKo1udiz", 
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
            
    data["database"] = "your_database"
    data["name"] = "your_name"
    data["url"] = "your_URL"


    cl.addDataSource(data)
    new_dashboard = cl.updateDashboard(dashboard)

    print(new_dashboard)
    return "SUCCESSFULL"

