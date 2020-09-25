version = $(shell cat VERSION)
docker_tag = junte/pg-backup:$(version)

build:
	@docker build -t $(docker_tag) .

publish:
	@docker push $(docker_tag)

tag:
	git push && git tag -a $(version) -m $(version) && git push --tags