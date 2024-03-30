from kubernetes import client, config

def delete_pod(pod_name, namespace='default'):
    config.load_kube_config()  # Loads the current kubeconfig
    v1 = client.CoreV1Api()
    delete_options = client.V1DeleteOptions()
    try:
        v1.delete_namespaced_pod(pod_name, namespace, body=delete_options)
        print(f"Pod {pod_name} deleted.")
    except client.exceptions.ApiException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pod_name = input("Enter the name of the pod to delete: ")
    delete_pod(pod_name)
