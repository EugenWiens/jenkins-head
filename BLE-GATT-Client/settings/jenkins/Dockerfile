FROM jenkins/jenkins:lts

ENV JENKINS_USER admin
ENV JENKINS_PASS admin

# Skip initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

COPY ./jobs /usr/share/jenkins/ref/jobs
COPY ./users /usr/share/jenkins/ref/users
COPY ./rootFiles/config.xml.override /usr/share/jenkins/ref/
COPY ./rootFiles/jenkins.security.apitoken.ApiTokenPropertyConfiguration.xml /usr/share/jenkins/
COPY ./rootFiles/jenkins.security.QueueItemAuthenticatorConfiguration.xml /usr/share/jenkins/
COPY ./rootFiles/jenkins.security.UpdateSiteWarningsConfiguration.xml /usr/share/jenkins/

