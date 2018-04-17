c = get_config()

c.NotebookApp.file_to_run = '/home/jovyan/data/index.ipynb'
c.NotebookApp.iopub_data_rate_limit=1.0e10

c.NotebookApp.allow_origin = '*'

c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestor 'self' https://notebooks.mpiwg-berlin.mpg.de; child-src *"
    }
}
