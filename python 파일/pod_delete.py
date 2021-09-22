from kubernetes import client, config

config.load_kube_config()


def delete_pod(name, namespace):
    core_v1 = client.CoreV1Api()
    # delete_options = client.V1DeleteOptions() 있는 것과 없는 것의 변화 x
    # print("delete option :", delete_options)
    api_response = core_v1.delete_namespaced_pod(
        name=name,
        namespace=namespace)
    # print(api_response)


if __name__ == '__main__':
    delete_pod(name='busybox-test', namespace='default')
