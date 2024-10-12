PY := python3
FLAGS := -b
SRC_DIR := src
CREATOR := $(SRC_DIR)/creator.py

DATA_DIR := data
LATEST_DATA_DIR := latest_data

REQUIREMENTS_FILE := requirements.txt


sure=0

.PHONY: init freeze create ship nuke_data nuke_latest_data

init:
	pip install -r $(REQUIREMENTS_FILE)


freeze:
	pip freeze > $(REQUIREMENTS_FILE)


create:
	@$(PY) $(FLAGS) $(CREATOR)


ship:
	@rm -rf $(LATEST_DATA_DIR)/*
	@cp -r $(DATA_DIR)/* $(LATEST_DATA_DIR)/


nuke_data:
	@([ $(sure) -eq 1 ] && rm -rf $(DATA_DIR)/*) || echo "Please set sure=1 to nuke data"


nuke_latest_data:
	@([ $(sure) -eq 1 ] && rm -rf $(LATEST_DATA_DIR)/*) || echo "Please set sure=1 to nuke data"
