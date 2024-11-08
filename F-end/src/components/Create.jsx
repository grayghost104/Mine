import { useNavigate } from 'react-router-dom' 
import { useState} from 'react';
import { Button,Label, TextInput } from "flowbite-react";




export default function New_user({there, setThere}) {
    const navigate = useNavigate()
    const [rusername, setRUsername] = useState("");
    const [rpassword, setRPassword] = useState("");
    const [email, setEmail] = useState("");
    const [sLI, setSLI] = useState(false);
    

    function Create(e){
        e.preventDefault();
        fetch('/user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email, 
                username: rusername,
                password: rpassword
            })
        })
        .then(r => {
            if (r.ok) {
                setRUsername("")
                setRPassword("")
                setEmail("")
                navigate('/home')
            }
            else{
                alert("Username or Password Invalid")
                return undefined
            }
        })
        .then(data=>setThere(data))
    }

    return (

        <form onSubmit={Create}>
        <Label value="Your email" /> 
        <TextInput
        id="email3"
        type="email"
        placeholder="name@flowbite.com"
        value={email} onChange={(e) => setEmail(e.target.value)}
        /> 
        <Label value="Your username" />
        <TextInput type="text" value={rusername} onChange={(e)=>setRUsername(e.target.value)} placeholder="Username"  id="username"/>
          <Label value="Your password" /> 
        <TextInput id="password"value={rpassword} onChange={(e) => setRPassword(e.target.value)}/>
           <input type="checkbox" onChange={(e)=>setSLI(!sLI)}/>
      <Button variant='primary' className='mt-3' type="submit">Create New User</Button>
    </form>

    )
}