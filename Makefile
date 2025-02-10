install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code

make lint:
	uv run ruff check brain_games

make lint-fix:
	uv run ruff check --fix brain_games