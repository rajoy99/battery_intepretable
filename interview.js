const imageGetter = () => {

  const [imagefile, setimagefile] = useState("");
  useEffect(() => {
    fetch("s3domain/relative-path/filename.jpg")
      .then((response) => response.blob())
      .then((image) => {
        // Create a local URL of that image
        const localUrl = URL.createObjectURL(image);
        setimagefile(localUrl);
      });
  }, []);

  return (
    <Fragment>
      <img src={imagefile} alt="Image Name"/>
    </Fragment>
  );
};
