Notebook Image Collection
=========================

Provides docker images for the notebooks presented at notebookPresentServer.
Images have to be build on the server, using the tag eoa.
For example, to build the webCrawl image, clone the repository to the server hosting
the presentServer, change in the corresponding folder and run
  ```
  docker build -t eoa/websources .
  ```

This will make the image automatically available for selection in the drop-down.

Structure of a publication
--------------------------

Each publication has the following structure
```
publication/
├── config
│   └── jupyter_notebook_config.py
├── data
│   └── index.ipynb
|   └── example_data.csv
├── Dockerfile
└── packages
    └── requirements.txt

```

The file to be displayed is `index.ipynb`. This can be the title page of a book with several chapters as well as a simple recipe for working with a specific dataset.
The data to be processed by the notebook should in general be loaded from websources
or DOI. If that is not possible, additional data files can be added to the docker image.

The required python packages are listed in `requirements.txt`.

Additionally, one could require Linux packages to be installed by `apt` into the docker image, e.g., for compiled code for network analysis or machine learning, in a file `packages.txt`. In this case the follwing lines have to uncommented in the Dockerfile:
```
sudo dpkg --set-selections < /srv/packages.txt
sudo apt-get -u dselect-upgrade  
```

Working with styles
-------------------

If necessary, it is possible to add custom designs to Jupyter Notebooks. For an example, have a look at the [fullExample config](../fullExample/config/custom).

JupyterHub accepts a custom CSS file, e.g., for custom color schemes or logos, as well as a custom JS file, e.g., to define custom buttons or helper functions. The styles are loaded using the Dockerfile.

Further work :soon: :grin:
---
* Create a set of base images with standard packages for
  * networks
  * natural language processing
  * image processing
  * 3D mesh and pointcloud analysis
  * geographic information systems
- Create a set of designs
