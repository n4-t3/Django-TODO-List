FROM python:3.8

#directory in the container you want to workout of
WORKDIR /usr/src/DJANGO-TODO-LIST/TODO_List/

#disables Python's output buffering and is immediately written
ENV PYTHONUNBUFFERED 1 

#prevent the creation of bytecode files( used to improve the startup time of Python scripts)
ENV PYTHONDONTWEITEBYTCODE 1

#copy everything in the root directory to the WORKDIR
COPY ./ ./ 

# Install packages
RUN pip install -r Requirements.txt

CMD ["/bin/bash"]
