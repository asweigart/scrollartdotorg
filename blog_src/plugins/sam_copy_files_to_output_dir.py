from pelican import signals
import shutil, os

def copy_files_to_output_dir(sender):
    print('sam_copy_files_to_output_dir.py: Copying files to output dir (' + sender.settings.get('OUTPUT_PATH') + ')')
    # I'll add files here as needed.
    shutil.copyfile(os.path.join(os.path.dirname(__file__), 'favicon.ico'), 
                                 os.path.join(sender.settings.get('OUTPUT_PATH'), 'favicon.ico'))

def register():
    signals.initialized.connect(copy_files_to_output_dir)
