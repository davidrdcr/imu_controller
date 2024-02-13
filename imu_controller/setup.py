from setuptools import setup

package_name = 'imu_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu200422',
    maintainer_email='ubuntu200422@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_node = imu_controller.imu_node:main'
            #imu_node es el nombre del nodo que ejecutaremos
            #imu_controller.imu_node es el nombre del paquete y el nombre del archivo que contiene el nodo
        ],
    },
)