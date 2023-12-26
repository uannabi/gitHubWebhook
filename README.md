# Flask GitHub Webhook Demonstrator
Welcome to the Flask GitHub Webhook Demonstrator repository! This project is a Flask application designed to illustrate the functionality of GitHub webhooks in a simple, interactive manner.

## About This Project
GitHub webhooks are powerful tools for automating workflows and integrating various services. This Flask application serves as a hands-on guide to understanding how GitHub webhooks trigger actions in real-time. It's an ideal resource for developers looking to integrate GitHub webhooks into their projects or for educational purposes.

## Key Features
- Simple Flask web application.
- Real-time demonstration of GitHub webhook triggers.
- Easy-to-understand codebase for learning and modification.

## Getting Started
Prerequisites
- Python 3.x
- Flask
- ngrok (for exposing local server to the internet)
- Installation and Setup
- Clone the Repository

```
git clone https://github.com/uannabi/gitHubWebhook.git
Install Required Libraries
```
Navigate to the cloned directory and install the required libraries:

```
pip install -r requirements.txt
```
## Setting Up the Webhook

Go to your GitHub repository > Settings > Webhooks.
Add a new webhook and set the payload URL to your ngrok or public server URL.
Choose the events you want to trigger the webhook.
Run the Flask App

## Start the Flask application:

```

flask run
```
Expose Your Local Server (Optional)

If you are using ngrok:

```
ngrok http 5000
```
Update the webhook's payload URL with the ngrok URL.

## Usage
Once everything is set up, perform actions in your GitHub repository to trigger the webhook. The Flask app will receive the payloads and you can see how the webhook reacts in real-time.

## Contributing
If you have suggestions for how this project could be improved, or want to report a bug, feel free to fork this repository and submit a pull request.
