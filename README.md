# Furby Connect World CDN
This is a full archive of the entire Furby Connect World APP CDN


Using a proxy server I was able to see that the app downloads the majority of its files, assets and DLCs from `https://furbyapp.s3.amazonaws.com/`.

Luckily for me, this was an S3 bucket with indexing enabled, so using two Python scripts, `s3-indexer.py` and `s3-downloader.py` I was able to download an entire copy of the CDN, so the app can still be used after these servers innevitably go offline and also as an archive of every DLC file created for the Furby.


### Staging?
As the app is officially discontinued, all DLCs from staging that I am aware off were put into live, so staging should be identical to live, however, there _is_ an `osx` set of assetbundles, presumably to run on a Mac for development purposes. Further research is required.