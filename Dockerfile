# dependencies stage
# this converts the pipenv dependencies to requirements.txt so we don't have to bundle pipenv in the prod image
FROM python:3.10.12-slim as depends

WORKDIR /setup
RUN pip install pipenv
COPY Pipfile Pipfile.lock .
RUN pipenv requirements > requirements.txt

# prod stage
# this gets shipped to the robot
FROM python:3.10.12-slim
WORKDIR /build

# python dependencies setup
RUN uname -a
RUN pip install viam-sdk==0.4.8
COPY --from=depends /setup/requirements.txt .
RUN pip install --no-cache -r requirements.txt

# copy production code
COPY module/ module/
CMD python -m module
