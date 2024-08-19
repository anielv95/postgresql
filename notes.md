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