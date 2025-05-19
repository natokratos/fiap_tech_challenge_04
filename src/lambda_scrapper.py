import json
import boto3

def lambda_handler(event, context):
    # Initialize a boto3 client for AWS Glue
    lambda_client = boto3.client('glue')
    
    # Name of your Glue job
    glue_job_name = 'extraction-job'
    
    try:
        # Start the Scrapper
        #scraper = Scrapper()

        #dest_files = scraper.run()

        #for f in dest_files:
        #    if "Dia_" in f and ".parquet" not in f:
        #        aws_s3 = AwsS3()
        #        aws_s3.upload_file("raw", f)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Founded files',
            #    'Files': dest_files
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error obtaining data',
                'error': str(e)
            })
        }
    
if __name__ == '__main__':
    event = {}
    context = None
    print(lambda_handler(event, context))