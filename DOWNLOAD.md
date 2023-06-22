Dataset **BCCD** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/d/Q/i0/4P7VSYcX7dnqjt6Z642VPAR5hrtTFzvyEJTcIdfNTZzzTfNRow5sdkRP6ibC1S5EfBn69z8IE7U65Vlc6yoNUpfr6hPbfdXSXxOGF24sTbwGPnB2ra7CxXk9cWyY.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='BCCD', dst_path='~/dtools/datasets/BCCD.tar')
```
The data in original format can be 🔗[downloaded here](https://github.com/Shenggan/BCCD_Dataset/archive/refs/tags/v1.0.zip)