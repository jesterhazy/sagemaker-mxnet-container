import container_support as cs
import os


class MXNetHostingEnvironment(cs.HostingEnvironment):
    DEFAULT_MODEL_FIRST_DIMENSION_SIZE_PARAM = "SAGEMAKER_DEFAULT_MODEL_FIRST_DIMENSION_SIZE"

    def __init__(self, base_dir=cs.ContainerEnvironment.BASE_DIRECTORY):
        super(MXNetHostingEnvironment, self).__init__(base_dir)
        self.preferred_batch_size = int(os.environ.get(
            MXNetHostingEnvironment.DEFAULT_MODEL_FIRST_DIMENSION_SIZE_PARAM, '1'))

        self.update_mxnet_envvars()

    @staticmethod
    def update_mxnet_envvars():
        if not os.environ.get('MXNET_CPU_WORKER_NTHREADS'):
            os.environ['MXNET_CPU_WORKER_NTHREADS'] = '1'

        if not os.environ.get('MXNET_CPU_PRIORITY_NTHREADS'):
            os.environ['MXNET_CPU_PRIORITY_NTHREADS'] = '1'

        if not os.environ.get('MXNET_KVSTORE_REDUCTION_NTHREADS'):
            os.environ['MXNET_KVSTORE_REDUCTION_NTHREADS'] = '1'

        if not os.environ.get('MXNET_ENGINE_TYPE'):
            os.environ['MXNET_ENGINE_TYPE'] = 'NaiveEngine'

        if not os.environ.get('OMP_NUM_THREADS'):
            os.environ['OMP_NUM_THREADS'] = '1'
