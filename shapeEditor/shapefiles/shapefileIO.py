def import_data(shapefile):
    fd,fname = tempfile.mkstemp(suffix=".zip")
    os.close(fd)
    f = open(fname, "wb")
    for chunk in shapefile.chunks():
        f.write(chunk)
        f.close()
    return 