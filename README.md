# K8s Self-Healing Simulator

The Kubernetes Self-Healing Simulator is a Python CLI tool designed to demonstrate the self-healing capabilities of Kubernetes that I developed for customer workshops. It allows users to delete a pod from a list of running pods and then watch as Kubernetes automatically recreates the pod, showcasing the system's resilience.

## Features

- List all running pods in a specified namespace.
- Delete a selected pod and observe Kubernetes' response to maintain the desired state.
- Watch and display events related to the pod's recreation process.

## Prerequisites

- Python 3.6+
- Kubernetes cluster (Minikube or any cloud-based Kubernetes service)
- kubectl configured to connect to your Kubernetes cluster
- Kubernetes Python client

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/kubernetes-self-healing-simulator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd kubernetes-self-healing-simulator
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your `kubectl` is configured and points to the desired Kubernetes cluster.
2. Run the simulator:
   ```bash
   python src/simulator.py
   ```
3. Follow the on-screen prompts to select and delete a pod. Observe the self-healing process through event logs.

## Contributing

Contributions to the Kubernetes Self-Healing Simulator are welcome! Please feel free to submit issues, pull requests, or enhancements to improve the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
