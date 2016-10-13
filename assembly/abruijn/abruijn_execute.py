#!/usr/bin/env python
from doepipeline.generator import PipelineGenerator
from doepipeline.executor import SSHExecutor
import os
import yaml
import sys
from datetime import datetime

if __name__ == '__main__':
    iterations = 0
    generator = PipelineGenerator.from_yaml(os.path.abspath('abruijn_pipeline_slurm.yaml'))
    designer = generator.new_designer_from_config()
    converged = False

    while not converged and iterations < 15:
        iterations += 1
        print ('========================================================================')
        print ('=')
        print ('= Iteration:', iterations)
        print ('= Starting:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print ('=')
        print ('========================================================================')

        design = designer.new_design()
        print ('design: {}'.format(design))
        designfilename="doe_design_" + str(iterations) + ".txt"
        design.to_csv(designfilename)

        pipeline = generator.new_pipeline_collection(design)
        
        # Pass the path to the uppmax.yaml as an argument to the script
        executor = SSHExecutor(yaml.load(open(os.path.abspath(sys.argv[1]))),
                           execution_type='slurm',
                           base_command='nohup {script}')
        results = executor.run_pipeline_collection(pipeline)
        print (results)

        filename="doe_result_" + str(iterations) + ".txt"
        results.to_csv(filename)
        optimum = designer.update_factors_from_response(results)
        print (optimum)
        converged = optimum.converged
        print (optimum.converged)

