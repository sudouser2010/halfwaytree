Install Instructions Using Vagrant
===========

####These instructions show you how to install Halfwaytree and test it on a brand-new virtual Ubuntu environment. Using Vagrant reduces the likelihood that you'll have issues installing Halfwaytree. If you don't have Vagrant installed see my video tutorial: https://www.youtube.com/watch?v=5udMlaqCg8M

Assumptions:<br>
1. you have Vagrant installed<br>
2. you have connection to the internet<br>
3. You don't have Halfwaytree downloaded yet
<br><br>

(0) Activate Virtual Machine
```
vagrant init hashicorp/precise32
vagrant up
vagrant ssh
```

(1) Update Virtual Machine
```
sudo apt-get update
sudo apt-get upgrade 
#(takes a long time, select continue without installing grub)
```

(2) Download and Install Pygraphviz
```
sudo apt-get install python-dev
sudo apt-get install -y graphviz libgraphviz-dev pkg-config python-pip
sudo pip install pygraphviz
```

(3) Download and Install Git
```
sudo apt-get install git-core
```

(4) Download and Install Z3
```
sudo apt-get install build-essential

git clone https://github.com/Z3Prover/z3.git
cd z3    
python scripts/mk_make.py
cd build
make   #(this takes a long time as well !)
sudo make install
cd ../../
```

(5) Download and Install Halfwaytree
```
git clone https://github.com/sudouser2010/halfwaytree.git
```

(6) Verify Halfwaytree Works
```
cd halfwaytree
python example.py

#This should produce an image in your folder called example.png

#note if you get a Segmentation fault error here, 
#then reinstall Pygraphviz with "sudo pip install pygraphviz" 
#and try again
```

