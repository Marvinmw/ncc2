import task_utils
from absl import app
from absl import flags

def main(argv):
    del argv    # unused
    data = "llvm_ir"
    task_utils.llvm_ir_to_trainable(data)
if __name__ == "__main__":
    app.run(main)