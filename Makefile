version = 1.5-client12

build:
	@docker build -t junte/pg-backup:$(version) .

publish:
	@docker push junte/pg-backup:$(version)