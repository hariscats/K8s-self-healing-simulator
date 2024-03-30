from kubernetes import client, config
from kubernetes import watch
import time

def list_pods(namespace='default'):
    config.load_kube_config()  # Loads kubeconfig from file
    v1 = client.CoreV1Api()
    print("Fetching pod list...")
    pods = v1.list_namespaced_pod(namespace)
    for i, pod in enumerate(pods.items):
        print(f"{i}: {pod.metadata.name}")
    return pods.items

def delete_pod(pods, index, namespace='default'):
    pod_name = pods[index].metadata.name
    v1 = client.CoreV1Api()
    delete_options = client.V1DeleteOptions()
    try:
        v1.delete_namespaced_pod(pod_name, namespace, body=delete_options)
        print(f"Pod {pod_name} deleted. Waiting for recreation...")
    except client.exceptions.ApiException as e:
        print(f"An error occurred: {e}")
        return None
    return pod_name

def watch_pod_events(pod_name, namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()
    print(f"Watching events for new pod creation...")
    for event in w.stream(v1.list_namespaced_event, namespace=namespace, timeout_seconds=60):
        if event['object'].involved_object.name == pod_name and event['object'].reason in ['Scheduled', 'Created', 'Started']:
            print(f"Event: {event['object'].reason}, Message: {event['object'].message}")
            if event['object'].reason == 'Started':  # Assuming 'Started' indicates the pod is recreated and running
                w.stop()
                print("Pod recreation detected. Watching stopped.")

if __name__ == "__main__":
    namespace = 'default'  # Change this as needed
    pods = list_pods(namespace)
    if not pods:
        print("No pods found.")
        exit()
    
    pod_index = int(input("Enter the number of the pod to delete: "))
    if pod_index < 0 or pod_index >= len(pods):
        print("Invalid selection.")
        exit()

    deleted_pod_name = delete_pod(pods, pod_index, namespace)
    if deleted_pod_name:
        # Sleep for a few seconds to allow the deletion event to propagate
        time.sleep(5)
        watch_pod_events(deleted_pod_name, namespace)
