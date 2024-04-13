Postmortem: Unexpected Web Service downtime
Issue Summary
  Duration:
      o	Start Time: 13-4-2024, 2:45
      o	End Time: 13-4-2024, 3:45
  Impact:
      o	The web service experienced downtime
      o	About 10% of users were affected during the outage.
      o	The Nginx service on the Ubuntu container was down, resulting in connection errors for users attempting to access the web server.
  Timeline
    Detection:
      o	The issue was detected at 13-4-2024 through automated monitoring alerts.
    Actions Taken:
      o	Investigated server logs for any unusual activity or errors.
      o	Assumed the issue might be related to a recent deployment.
    Misleading Paths:
      o	Checked for recent code changes in the deployed version.
    Escalation:
      o	The incident was escalated to the Development team after initial investigation.
    Resolution:
      o	Rolled back to the previous stable version of the application.
      o	Restarted the necessary services to apply the rollback.
  Root Cause and Resolution
    Root Cause:
      o	A recent code deployment introduced a bug, causing the application to crash under certain conditions.
    Resolution:
      o	Rolled back to the previous version, eliminating the introduced bug.
      o	Restarted the necessary services to apply the rollback.
  Corrective and Preventative Measures
    Improvements/Fixes:
      o	Automated testing procedures to include more scenarios.
      o	Strengthen monitoring for application health and performance.
    Tasks:
      o	make a review of the deployment process to ensure code changes are adequately tested before release.
      o	Schedule regular audits of the application's error logs to proactively identify potential issues.
      o	Implement a post-deployment validation step to verify the stability of the application.
In conclusion, 
the unexpected downtime was promptly addressed by rolling back to a stable version and implementing additional testing measures. The incident underscores the importance of thorough testing in the deployment process and ongoing vigilance through robust monitoring.

