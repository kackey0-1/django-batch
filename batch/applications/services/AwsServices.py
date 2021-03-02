import datetime
import calendar
import boto3
from botocore.config import Config

config = Config(retries={
                        'max_attempts': 10,
                        'mode': 'standard'})
session = boto3.client('ce', config=config)


if __name__ == '__main__':

    today = datetime.date.today()
    month_start = today.strftime('%Y-%m-01')
    month_end = today.strftime('%Y-%m-{}').format(str(calendar.monthrange(today.year, today.month)[1]))
    print(month_start)
    print(month_end)
    response = session.get_cost_and_usage_with_resources(
        TimePeriod={
            'Start': month_start,
            'End': month_end
        },
        Filter={
        })
    print(response)
