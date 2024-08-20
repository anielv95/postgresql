1. OS details:

    ```cat /etc/os-release```

2. Install `gcloud`. For interactive mode execute:

    ```
    apt-get update
    
    apt-get install apt-transport-https ca-certificates gnupg curl
    
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
    
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    apt-get update && apt-get install google-cloud-cli
    ```

3. Install `gcloud`. For non interactive mode (Docker image) execute:

    ```
    apt-get update
    
    apt-get install apt-transport-https ca-certificates gnupg curl

    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && apt-get update -y && apt-get install google-cloud-cli -y
    ```

4. Sign in:

    ```
    gcloud init
    ```

5. Create the instance:

    ```
    gcloud sql instances create INSTANCE_NAME \
    --database-version=POSTGRES_15 \
    --region=REGION \
    --zone=ZONE \
    --tier=TIER \
    --edition=ENTERPRISE_PLUS
    ```

6. if intrested in explore zones:

    ```
    gcloud compute zones list
    ```

7. if intrested in explore regions:

    ```
    gcloud compute regions list
    ```

8. list tiers:

    ```
    gcloud sql tiers list
    ```

<!-- gcloud sql instances create pgvec \
--database-version=POSTGRES_15 \
--region=us-east1 \
--tier=db-f1-micro -->

9. list instance users:

    ```
    gcloud sql users list \
    --instance=INSTANCE_NAME
    ```

10. set password for default user:

    ```
    gcloud sql users set-password postgres \
    --instance=INSTANCE_NAME \
    --prompt-for-password
    ```

11. create user:
    ```
    gcloud sql users create USER_NAME \
    --instance=INSTANCE_NAME \
    --password=PASSWORD
    ```

12. 