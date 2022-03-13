import React, { useState, useEffect, useRef } from 'react';
import AntHeader from '../components/header/AntHeader';
import Footer from '../components/footer/Footer';
import DefaultImage from '../assets/images/dashboard/test.JPEG'
import DefaultImageResult from '../assets/images/dashboard/result.JPEG'
import { Upload, message, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import axios from "axios";


const Dashboard = () => {
    const [urlFileObject, setUrlFileObject] = useState(DefaultImage)
    const [urlFileObjectResult, setUrlFileObjectResult] = useState(DefaultImageResult)
    const [progress, setProgress] = useState(0);
    const [predict, setPredict] = useState(false);
    let sessionIdRef = useRef(null)
    let processRef = useRef(null)


    const handleChange = ({file}) => {
        const url = URL.createObjectURL(file.originFileObj)
        setUrlFileObject(url)
        setUrlFileObjectResult(null)
    }

    const beforeUpload = (file) => {
        const isJPG = file.type === 'image/jpeg' || file.type === 'image/png';
        if (!isJPG) {
            message.error('You can only upload JPG or PNG file!');
            return false;
        } else {
            return true;
        }
    }
    const startUpload = async options => {
        const { onSuccess, onError, file, onProgress } = options;
        let fmData = new FormData();
        fmData.append("file", file);
        const config = {
            headers: { "content-type": "multipart/form-data" },
            onUploadProgress: event => {
              const percent = Math.floor((event.loaded / event.total) * 100);
              setProgress(percent);
              if (percent === 100) {
                setTimeout(() => setProgress(0), 1000);
              }
              onProgress({ percent: (event.loaded / event.total) * 100 });
            }
        };
        try {
            const res = await axios.post(
              "http://localhost:8081/api/v1/object-detection/process",
              fmData,
              config
            );
            onSuccess("Ok");
            console.log("server res: ", res, progress);
            sessionIdRef.current = res.data.task_id
            setPredict(true)
        } catch (err) {
            console.log("Eroor: ", err);
            const error = new Error("Some error");
            console.log(error)
            onError({ err });
        }
    }

    const getStatusSession = (sessionId, onUploadProgress) => {
        return axios.create({
          baseURL: "http://localhost:8081/api/v1/",
          }).get("object-detection/status/" + sessionId, {
          headers: {
            "accept": "application/json",
          },
          onUploadProgress,
        }).then(response => {
          return response
        }).catch(function (error) {
          return error.response
        });
      }

    const stopLoading = () => {
        clearInterval(processRef.current)
        setPredict(false)
    }

    useEffect(() => {
        if (predict === true){
             processRef.current = setInterval(() => {
                getStatusSession(sessionIdRef.current, (event) => {})
                .then((response) => {
                    setUrlFileObjectResult(response.data.detection_draw_url)
                    if (response.data.status.general_status === "SUCCESS" || response.data.status.general_status === "FAILED") 
                        stopLoading()
                })
            }, 3000)
        }
        else stopLoading()
    }, [predict]);

    return (
        <div className='dashboard'>
            <AntHeader/>
            <div className='col-one'>
                <div className='item'>
                    <div className='item-box'>
                        <div className='title'>
                            <h1>Select Image</h1>
                            <Upload 
                             name="test"
                             showUploadList={false}
                             onChange={handleChange}
                             beforeUpload={beforeUpload}
                             customRequest={startUpload}
                            >
                                <Button icon={<UploadOutlined />}>Select File</Button>
                            </Upload>
                        </div>
                        <div className='image'>
                            <img src={urlFileObject} alt=''></img>
                        </div>
                    </div>
                </div>
                <div className='item'>
                    <div className='item-box'>
                        <h1 className='title'>Result Image</h1>
                        <div className='image'>
                            <img src={urlFileObjectResult} alt=''></img>
                        </div>
                    </div>
                </div>
            </div>
            <Footer/>
        </div>
    );
}

export default Dashboard;
