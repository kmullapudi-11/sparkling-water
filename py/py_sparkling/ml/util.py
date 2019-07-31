from pyspark.ml.util import JavaMLReader, MLReadable


class JavaH2OMLReadable(MLReadable):
    """
    Special version of JavaMLReadable to be able to load pipelines exported together with H2O pipeline stages
    """

    def __init__(self):
        super(JavaH2OMLReadable, self).__init__()

    """
    (Private) Mixin for instances that provide JavaH2OMLReader.
    """

    @classmethod
    def read(cls):
        """Returns an MLReader instance for this class."""
        return JavaH2OMLReader(cls)


class JavaH2OMLReader(JavaMLReader):

    def __init__(self, clazz):
        super(JavaH2OMLReader, self).__init__(clazz)
        self._clazz = clazz
        self._jread = self._load_java_obj(clazz).read()

    @classmethod
    def _java_loader_class(cls, clazz):
        """
        Returns the full class name of the Java ML instance. The default
        implementation replaces "pyspark" by "org.apache.spark" in
        the Python full class name.
        """
        java_package = clazz.__module__.replace("pysparkling", "py_sparkling")
        if clazz.__name__ in ("Pipeline", "PipelineModel"):
            # Remove the last package name "pipeline" for Pipeline and PipelineModel.
            java_package = ".".join(java_package.split(".")[0:-1])
        return java_package + "." + clazz.__name__
