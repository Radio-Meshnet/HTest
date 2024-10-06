x:
	make devapk
	buildozer android deploy
	buildozer android logcat | grep "python"

all: prepare debug

prepare: activate

clean:
	@echo Cleaning...
	-(rm ./__pycache__ -r)
	-(rm ./bin -r)

cleanlibs:
	buildozer android clean

cleanall: clean cleanlibs

activate:
	(. venv/bin/activate)

debug:
	buildozer android debug

release:
	buildozer android release

apk: prepare release

devapk: prepare debug
