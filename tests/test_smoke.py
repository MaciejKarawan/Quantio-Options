from pathlib import Path
import ast, importlib, unittest
ROOT = Path(__file__).resolve().parents[1]
class SmokeTests(unittest.TestCase):
    def test_python_compiles(self):
        for directory in ['src','scripts']:
            for f in (ROOT/directory).rglob('*.py'):compile(f.read_text(encoding='utf-8-sig'),str(f),'exec')

    def test_imports_and_inputs(self):
        import quanto_options.pricing, quanto_options.hedging, quanto_options.simulation
        import scripts.run_analysis
        from quanto_options.paths import DATA
        self.assertTrue((DATA/'xauusd_d.csv').is_file())
        self.assertTrue((DATA/'usdpln_d.csv').is_file())

if __name__ == '__main__':unittest.main()
