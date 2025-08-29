### Zip
To zip using the best compression algorithm:

```bash
sudo 7z a -t7z -mx=9 -mfb=273 -ms -md=31 -myx=9 -mtm=- -mmt -mmtf -md=1536m -mmf=bt3 -mmc=10000 -mpb=0 -mlc=0 dir.7z dir
```

To create the smallest standard ZIP file that 7-Zip can create, try:

```bash
7z a -mm=Deflate -mfb=258 -mpass=15 -r foo.zip C:\Path\To\Files\*
```
Otherwise if you don't care about the ZIP standard, use the following ultra settings:

7z a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on archive.7z dir1
Which are:

```
-t7z   7z archive

-m0=lzma
       lzma method

-mx=9  level of compression = 9 (Ultra)

-mfb=64
       number of fast bytes for LZMA = 64
-md=32m
       dictionary size = 32 megabytes

-ms=on solid archive = on
```
