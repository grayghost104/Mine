import { Sidebar } from "flowbite-react";
import { BiBuoy } from "react-icons/bi";
import { useEffect } from "react";
import { HiChartPie, HiInbox, HiUser, HiViewBoards, HiArrowSmRight } from "react-icons/hi";

export default function Head({setThere}) {
    console.log(setThere)
    const background = document.body.style.backgroundImage = "url('https://images.pluto.tv/series/63910b784f35ef001368d31c/featuredImage.jpg?fill=blur&fit=fill&fm=jpg&q=75&w=1200)";
    useEffect(() => {
      document.body.style.backgroundImage = "url('https://images.pluto.tv/series/63910b784f35ef001368d31c/featuredImage.jpg?fill=blur&fit=fill&fm=jpg&q=75&w=1200)";
      
      // Cleanup background image on component unmount
      return () => {
          document.body.style.backgroundImage = "";
      };
  }, []);

  return (
    <>
        <div>
        <Sidebar aria-label="Default sidebar example">
      <Sidebar.Items>
        <Sidebar.ItemGroup>
          <Sidebar.Item href="/buy" icon={HiChartPie}>
            Buy
          </Sidebar.Item>
          <Sidebar.Item href="/monster" icon={HiViewBoards} labelColor="dark">
            Monsters
          </Sidebar.Item>
          <Sidebar.Item href="/story" icon={HiArrowSmRight}>
            Story
          </Sidebar.Item>
          <Sidebar.Item href="/media" icon={HiInbox}>
            Movies and episodes
          </Sidebar.Item>
          <Sidebar.Item href="/" icon={HiUser}>
            Login/Register
          </Sidebar.Item>
          <Sidebar.Item href="/home" icon={BiBuoy}>
            Home
          </Sidebar.Item>
        </Sidebar.ItemGroup>
      </Sidebar.Items>
    </Sidebar>
    </div>
    </>
  )
}

