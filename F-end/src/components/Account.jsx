import { useNavigate } from 'react-router-dom' 
import { useState} from 'react';
import { Button,Label, TextInput } from "flowbite-react";
import 

function Account({there, setThere}) {
    const navigate = useNavigate()
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [sLI, setSLI] = useState(false);


    function Login(e){
        e.preventDefault();
        fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: username,
            password: password, 
            stayLoggedIN: sLI
          })
        })
        .then(r=>{
          if (r.ok) { return r.json()}
          else {throw new Error()}
        })
        .then(data=>{
          console.log(data)
          setThere(data)
          navigate('/home')
        })
        .catch(data=>{
          alert('Invalid Username or Password')
        })
    }

    return(
        <form onSubmit={Login}>
            <Label value="Your username" />
        <TextInput value={username} onChange={(e) => setUsername(e.target.value)} type='text' id="username"/>
          <Label value="Your password" />
        <TextInput value={password} onChange={(e) => setPassword(e.target.value)} type='text' id="password"/>
        <Label value="Stay logged in?" />
        <input type="checkbox" name='stayLoggedIn' value={sLI} onChange={e=>setSLI(!sLI)}/>
      <Button variant='primary' type="submit">Login</Button>


      <Button type="submit"  onClick={() => navigate('/create')} >Register new account</Button>
    </form>
    )
    
  }
  // helperText={
  //   <>
  //     We’ll never share your details. Read our
  //     <a href="#" className="ml-1 font-medium text-cyan-600 hover:underline dark:text-cyan-500">
  //       Privacy Policy
  //     </a>
  //     .
  //   </>
  // }
export default Account;