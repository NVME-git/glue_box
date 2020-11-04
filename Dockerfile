FROM amazon/aws-glue-libs:glue_libs_1.0.0_image_01
WORKDIR /home/jupyter/jupyter_default_dir  
EXPOSE 8888
EXPOSE 4040
CMD ["/home/jupyter/jupyter_start.sh"]
