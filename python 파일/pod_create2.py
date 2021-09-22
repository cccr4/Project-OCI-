from kubernetes import client, config

config.load_kube_config()


def create_pod(name, namespace):
    corev1 = client.CoreV1Api()
    pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'image': 'busybox',
                    'name': 'sleep',
                    "args": [
                        "/bin/sh",
                        "-c",
                        "while true;do date;sleep 5; done"
                    ]
                }]
            }
        }


    api_response = corev1.create_namespaced_pod(body=pod_manifest,
                                                  namespace='default')

if __name__ == '__main__':
    create_pod(name='busybox-test', namespace='default')
