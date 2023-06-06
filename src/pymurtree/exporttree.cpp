#include "exporttree.h"

void ExportTree::exportText(MurTree::DecisionNode* tree, std::string filepath) {

    if (tree == nullptr) {
        return;
    }

    try {
        if (filepath.empty()) {
            ExportTree tmp(tree, &std::cout, true);
        }
        else {
            std::ofstream ofs(filepath, std::ofstream::out);
            if(!ofs.is_open() || ofs.fail()){
                throw std::runtime_error("Failed to open text output file.");        
            }
	        ExportTree tmp(tree, &ofs, true);
	        ofs.close();	
        }
    }
    catch(std::runtime_error err) {
        std::cout << "Failed to write text output file. Message: "
              << err.what() << std::endl;
    }

}

void ExportTree::exportDOT(MurTree::DecisionNode* tree, std::string filepath) {}


ExportTree::ExportTree(MurTree::DecisionNode* tree, std::ostream* os, bool textformat)
    : m_tree(tree), m_os(os)
{
    if(textformat) {
        // print right-side first
        writeEdge(tree, true, 0);
        writeEdge(tree, false, 0);
    }
}

void ExportTree::writeEdge(MurTree::DecisionNode* parentnode, bool rightedge, unsigned int indentationlevel) {

    // iterate over the edges of the tree

    if(parentnode == nullptr) {
        return;
    }

    std::string output = "|---";

    if(parentnode->IsLabelNode()) {
        output.append("class: " + std::to_string(parentnode->label_));
    }
    else {
        output.append("feature #" + std::to_string(parentnode->feature_) + " is ");
        rightedge ? output.append("present") : output.append("missing");  
    }

    for (int i = 0; i < indentationlevel; i++) {
        output.insert(0, "|   ");
    }
    output.append("\n");

    m_os->write(output.data(), output.size());

    if(parentnode->IsFeatureNode()) {
        if(rightedge){
            writeEdge(parentnode->right_child_, true, indentationlevel+1); 
            if(parentnode->right_child_->IsFeatureNode()){
                writeEdge(parentnode->right_child_, false, indentationlevel+1);
            }
        }
        else {
            writeEdge(parentnode->left_child_, true, indentationlevel+1); 
            if(parentnode->left_child_->IsFeatureNode()){
                writeEdge(parentnode->left_child_, false, indentationlevel+1);
            }
        }   
    }

}

