**Important**

The Dataset is obtained from: https://www.kaggle.com/andrewmvd/face-mask-detection
The Supporting code is obtained from: https://www.kaggle.com/daniel601/pytorch-fasterrcnn

This is not an original work but there are several changes made to optimize performance for the current system specs. (NVIDIA GeForce RTX 3080 Ti, Intel Core i7-10700K)

Note: To use BeautifulSoup4 to parse .xml, install lxml as a parser library using either pip or conda (whichever is suitable). Also, for Pytorch to have CUDA compute capability, install pytorch from source using the cuda toolkit
which is compatible with the NVIDIA GPU in the specifications.

USE torch.cuda.is_available() to check if CUDA capability is enabled. It should return True if properlr installed. Otherwise, set Device to "CPU" instead of "CUDA". (It will be way slower though..)