Dataset **BCCD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzExNDdfQkNDRC9iY2NkLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIm1Nd0o3dFk0MEFoR2JWWkRvdlJaNnpCL25JUFNKUHdCbG0zYUVWQjJYQkk9In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='BCCD', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://github.com/Shenggan/BCCD_Dataset/archive/refs/tags/v1.0.zip).