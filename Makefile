version = 1.5-client12
tag = junte/pg-backup:$(version)

build:
	@docker build -t $(tag) .

publish:
	@docker push $(tag)