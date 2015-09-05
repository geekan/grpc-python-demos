
echo "INFO: python 2.6+ and pip should be installed first."
echo "INFO: this script has been tested on ubuntu."

# install protobuf
git clone https://github.com/google/protobuf
cd protobuf
./autogen.sh
./configure
make
make check
make install
sudo ldconfig

cd python
python setup.py build
python setup.py test # if failed, try to update six by pip install -U six

python setup.py install
# OR do this:
# $ (cd .. && make install)
# $ python setup.py install --cpp_implementation

cd ../../



# install grpc itself
git clone https://github.com/grpc/grpc
cd grpc
git submodule update --init
make 
make install

apt-get install build-essential autoconf libtool
apt-get install python-all-dev python-virtualenv

CONFIG=opt tools/run_tests/build_python.sh 2.7
#./tools/run_tests/build_python.sh
