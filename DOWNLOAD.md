Dataset **BCCD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/d/Q/i0/4P7VSYcX7dnqjt6Z642VPAR5hrtTFzvyEJTcIdfNTZzzTfNRow5sdkRP6ibC1S5EfBn69z8IE7U65Vlc6yoNUpfr6hPbfdXSXxOGF24sTbwGPnB2ra7CxXk9cWyY.tar)

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

The data in original format can be [downloaded here](https://github.com/Shenggan/BCCD_Dataset/archive/refs/tags/v1.0.zip)