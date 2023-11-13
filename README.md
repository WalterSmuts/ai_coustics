;)

# AI Acoustics Client

This repository contains the mock implementation of the AI Acoustics client.

## Usage

from client import Client
from client_options import ClientOptions
from enhance_options import EnhanceOptions

client_options = ClientOptions({
"host": "https://api.ai-coustics.com",
"token": "YOUR_TOKEN"
})

client = Client(client_options)

enhance_options = EnhanceOptions({
"loudness": {
"enable": True,
"target_level": -16
},
"noise": {
"reduction": {
"enable": True,
"amount": "high"
}
}
})

client.enhance_file(
input="path/to/input.mp3",
output="path/to/output.mp3",
options=enhance_options
)