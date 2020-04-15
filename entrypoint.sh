touch /var/log/cron.log
ls -lA /var/log/cron.log
echo "Copying Datadog environment variables to /etc/environment"
printenv | grep DATADOG_ >> /etc/environment
echo "Starting cron..."
cron &
echo "tail -f /var/log/cron.log"
tail -f /var/log/cron.log
