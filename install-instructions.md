Install Instructions Without Vagrant
===========

Assumptions:<br>
1. you have connection to the internet<br>
2. You don't have Halfwaytree downloaded yet
<br><br>


(1) Download and Install Pygraphviz
```
sudo apt-get install python-dev
sudo apt-get install -y graphviz libgraphviz-dev pkg-config python-pip
sudo pip install pygraphviz
```

(2) Download and Install Git
```
sudo apt-get install git-core
```

(3) Download and Install Z3
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

(4) Download and Install Halfwaytree
```
git clone https://github.com/sudouser2010/halfwaytree.git
```

(5) Verify Halfwaytree Works
```
cd halfwaytree
python example.py

#This should produce an image in your folder called example.png

#note if you get a Segmentation fault error here, 
#then reinstall Pygraphviz with "sudo pip install pygraphviz" 
#and try again
```
