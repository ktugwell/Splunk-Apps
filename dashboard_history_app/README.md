# dashboard_history_app

Instructions
1) create an index called "version_history"
2) Be sure that the Search Head that hosts this app is forwarding it's logs to your indexer(s)
3) install the app, restart Splunk
4) The savedsearch "VH - Collect New Dashboard On Change" should be enabled on a 1 minute cron schedule
5) any changes to dashboards will now be logged, you can view these changes in the "Dashboard Version History" dashboard.


Limitations:
This method uses the "map" command. To avoid a lengthy search, it has been limited to 1 change per minute for 100 unique dashboards
