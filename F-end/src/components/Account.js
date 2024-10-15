import { useNavigate } from 'react-router-dom' 
import { useState} from 'react';

function Account({there, setThere}) {
    const navigate = useNavigate()
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [rusername, setRUsername] = useState("");
    const [rpassword, setRPassword] = useState("");
    const [email, setEmail] = useState("");
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
                // navigate('/monster')
            }
            else{
                alert("Username or Password Invalid")
                return undefined
            }
        })
        .then(data=>setThere(data))
    }

    return(
        <>
        {/* <h1>Monster High!</h1>
        <h3>Do you have a skullette key(login in)</h3> */}
        <form onSubmit={Login}>
            <Label value="Your username" />
        <TextInput value={username} onChange={(e) => setUsername(e.target.value)} type='text' id="username"/>
          <Label value="Your password" />
        <TextInput value={password} onChange={(e) => setPassword(e.target.value)} type='text' id="password"/>
        <input type="checkbox" name='stayLoggedIn' value={sLI} onChange={e=>setSLI(!sLI)}/>
      <Button variant='primary' type="submit">Login</Button>
      <Button type="submit">Register new account</Button>
    </form>



        {/* <h3>Or do you need help of your ghoulfriends to find one?(create an account)</h3> */}
        <form onSubmit={Create}>
        <Label value="Your email" /> 
        <TextInput id="email"value={email} onChange={(e) => setEmail(e.target.value)}/>
        <Label value="Your username" />
        <TextInput type="text" value={rusername} onChange={(e)=>setRUsername(e.target.value)} placeholder="Username"  id="username"/>
          <Label value="Your password" /> 
        <TextInput id="password"value={rpassword} onChange={(e) => setRPassword(e.target.value)}/>
           <input type="checkbox" onChange={(e)=>setSLI(!sLI)}/>
      <Button variant='primary' className='mt-3' type="submit">Create New User</Button>
    </form>
        
        </>
    )

}
export default Account;